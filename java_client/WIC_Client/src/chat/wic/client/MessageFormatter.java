package chat.wic.client;

import com.google.gson.*;

/**
 * Converts Message objects to json strings and
 * converts json strings to Message objects
 * @author Joe
 *
 */
public class MessageFormatter {
	
	Gson g;
	Message m;
	
	public MessageFormatter(){
		g = new Gson();
		m = new Message();
	}
	
	/**
	 * Converts json string to Message Object
	 * @param message
	 * @return
	 */
	public Message fromJson(String message){
		return g.fromJson(message, m.getClass());
	}
	
	/**
	 * Converts Message object to json String
	 * @param m
	 * @return
	 */
	public String toJson(Message m){
		return g.toJson(m);
	}
}
