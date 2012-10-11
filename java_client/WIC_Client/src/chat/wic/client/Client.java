package chat.wic.client;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

/**
 * Defines a multithreaded client that connects, sends/receives data from the server
 * @author Joe
 *
 */
public class Client{
	BufferedReader in;
	BufferedWriter out;
	Socket socket;
	String host;
	int port;
	String message;
	Frame parent;
	PrintWriter print;
	MessageFormatter mf;
	String username;
	
	public Client(String host, int port, Frame parent, String username) throws UnknownHostException, IOException{
		this.username = username;
		mf = new MessageFormatter();
		this.port = port;
		this.host = host;
		this.parent = parent;
		socket = new Socket(host, port);
		out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
		in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
		new Thread(new ListenFromServer()).start();
		
		out.write(mf.toJson(new Message(username, "")));
		out.flush();
	}
	
	/**
	 * sends a json object string to the server containing the parameter 'message'
	 * @param message
	 * @throws IOException
	 */
	public void sendToServer(String message) throws IOException{
		parent.convoBox.append(message+"\n");
		parent.inputField.setText("");
		out.write(mf.toJson(new Message(username, message)));
		out.flush();
	}
	
	/**
	 * Defines a Thread to check for data received from the server.
	 * @author Joe
	 *
	 */
	private class ListenFromServer implements Runnable{

		@Override
		public void run() {
			while(true){
				try {
					message = in.readLine();
					Message messageObject = mf.fromJson(message);
					if(!(messageObject.username.equals(username))){
						parent.convoBox.append(messageObject.username+">"+messageObject.message+"\n");
					}
					
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
		
	}
}