package chat.wic.client;

/**
 * defines a simple message that can be formatted to a json string
 * by a MessageFormatter
 * @author Joe
 *
 */
public class Message {
	String username;
	String message;
	
	public Message(String username, String message){
		this.username = username;
		this.message = message;
	}
	
	public Message(){
		
	}
}
