package chat.wic.client;

import java.awt.Color;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

import com.google.gson.Gson;

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
	
	public Client(Frame parent) throws UnknownHostException, IOException{
		Scanner sc = new Scanner(new BufferedReader(new FileReader("client.info")));
		Gson g = new Gson();
		String information = sc.nextLine();
		ClientInformation cl = new ClientInformation();
		cl = g.fromJson(information, cl.getClass());
		this.username = cl.username;
		mf = new MessageFormatter();
		this.port = cl.port;
		this.host = cl.host;
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
		parent.convoBox.append(username+"> "+message+"\n");
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
			try {
				while((message = in.readLine())!= null){
						
						Message messageObject = mf.fromJson(message);
						if(!(messageObject.username.equals(username))){
							parent.convoBox.append(messageObject.username+">"+messageObject.message+"\n");
							parent.convoBox.setCaretPosition(parent.convoBox.getDocument().getLength());//autoscrolling
						}
				}parent.convoBox.setBackground(Color.RED);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
	}
}
