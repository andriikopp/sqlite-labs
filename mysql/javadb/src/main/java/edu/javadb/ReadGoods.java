package edu.javadb;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class ReadGoods {

	public static void main(String[] args) {
		try {
			Class.forName("com.mysql.jdbc.Driver");
			Connection cn = null;

			try {
				cn = DriverManager.getConnection("jdbc:mysql://localhost/shopdb", "root", "");
				Statement st = cn.createStatement();
				ResultSet rs = st.executeQuery("SELECT * FROM goods");

				while (rs.next()) {
					System.out.println("ID: " + rs.getInt(1));
					System.out.println("Name: " + rs.getString(2));
					System.out.println("Price: " + rs.getDouble(3));
					System.out.println();
				}

				rs.close();
				st.close();
				cn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}
}
