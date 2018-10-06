package com.n9mtq4.checker;

import org.java_websocket.WebSocket;
import org.java_websocket.handshake.ClientHandshake;
import org.java_websocket.server.WebSocketServer;
import org.python.core.PyFunction;
import org.python.core.PyString;

import java.net.InetSocketAddress;
import java.util.ArrayList;

/**
 * Created by will on 10/6/18 at 3:47 PM.
 * 
 * Websocket server for access in processing.
 * very bad code. sorry
 * 
 * @author Will "n9Mtq4" Bresnahan
 */
public class CheckerWebsocketServer extends WebSocketServer {
	
	private final int port;
	private final PyFunction player1Lambda; // the python function for player 1
	private final PyFunction player2Lambda; // the python function for player 2
	
	private final ArrayList<WebSocket> playersSockets = new ArrayList<>();
	
	public CheckerWebsocketServer(int port, PyFunction player1Lambda, PyFunction player2Lambda) {
		super(new InetSocketAddress(port));
		this.port = port;
		this.player1Lambda = player1Lambda;
		this.player2Lambda = player2Lambda;
	}
	
	@Override
	public void onOpen(WebSocket conn, ClientHandshake handshake) {
		System.out.println("New Connection");
		if (playersSockets.size() >= 2) {
			System.out.println("Already two players, denying connection");
			conn.close();
			return;
		}
		playersSockets.add(conn);
		if (playersSockets.size() == 2) {
			System.out.println("All players joined, ready");
		}
	}
	
	@Override
	public void onClose(WebSocket conn, int code, String reason, boolean remote) {
		System.out.println(conn + " has disconnected");
	}
	
	@Override
	public void onMessage(WebSocket conn, String message) {
		
		System.out.println(conn + ": " + message);
		
		// only send to python when both players are connected
		if (playersSockets.size() < 2) {
			System.out.println("Not all players, joined. Not sending to p1 p2 funcs");
			return; // not all players joined
		}
		
		final int player = playersSockets.indexOf(conn);
		final PyFunction lambda = player == 1 ? player1Lambda : player2Lambda;
		lambda.__call__(new PyString(message));
		
	}
	
	public void broadcast(String msg) {
		for (int i = 0; i < playersSockets.size(); i++) {
			sendToPlayer(i, msg);
		}
	}
	
	/**
	 * Send a message to player 1
	 * */
	public void sendToPlayer1(String msg) {
		sendToPlayer(0, msg);
	}
	
	/**
	 * Send a message to player 2
	 * */
	public void sendToPlayer2(String msg) {
		sendToPlayer(1, msg);
	}
	
	private void sendToPlayer(int player, String msg) {
		final WebSocket conn = playersSockets.get(player);
		conn.send(msg);
	}
	
	@Override
	public void onError(WebSocket conn, Exception ex) {
		ex.printStackTrace();
	}
	
	@Override
	public void onStart() {
		System.out.println("Starting server");
		setConnectionLostTimeout(0);
		setConnectionLostTimeout(100);
	}
}
