package chat.wic.client;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.net.UnknownHostException;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

/**
 * Defines a Gui for the client to sit in. The client holds
 * a reference to a Frame object so that
 * it can add messages to the convoBox JTextArea
 * @author Joe
 *
 */
public class Frame extends JFrame {
	JTextField inputField;
	JTextArea convoBox;
	Client client;
	JScrollPane scroll;
	
	public Frame() throws UnknownHostException, IOException{
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setLayout(new BorderLayout());
		this.setSize(300, 400);
		inputField = new JTextField();
		convoBox = new JTextArea();
		convoBox.setEditable(false);
		inputField.addActionListener(new Handler());
		scroll = new JScrollPane(convoBox);
		add(inputField, BorderLayout.SOUTH);
		add(scroll, BorderLayout.CENTER);
		
		this.setVisible(true);
		
		client = new Client(this);
	}
	
	private class Handler implements ActionListener{

		@Override
		public void actionPerformed(ActionEvent e) {
			if(e.getSource() == inputField){
				try {
					client.sendToServer(inputField.getText());
				} catch (IOException e1) {
					e1.printStackTrace();
				}
			}
		}
	}
}
