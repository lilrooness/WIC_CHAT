package chat.wic.client;

import java.io.IOException;
import java.net.UnknownHostException;


public class Main {
	
	public static void main(String[] args) {
		try {
			new Frame();
		} catch (UnknownHostException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
