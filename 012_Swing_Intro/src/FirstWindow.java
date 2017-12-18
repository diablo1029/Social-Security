import java.awt.Color;

import java.awt.Insets;

import java.awt.GridBagLayout;
import java.awt.BorderLayout;
import javax.swing.JPanel;

import java.awt.GridBagConstraints;

import javax.swing.JFrame;
import javax.swing.JCheckBox;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.JRadioButton;

public class FirstWindow extends JFrame{

	public FirstWindow() {
		super("My computer is very special!");
		setSize(600, 400);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		JPanel p1 = new JPanel();
		p1.setBackground(Color.BLACK);
		
		JPanel p2 = new JPanel(new GridBagLayout() );
		p2.setBackground(Color.DARK_GRAY);

		JPanel p3 = new JPanel();
		p3.setBackground(Color.WHITE);
		
		JPanel p4 = new JPanel(new GridBagLayout() );
		p4.setBackground(Color.LIGHT_GRAY);
		
		JPanel p5 = new JPanel(new GridBagLayout() );
		p5.setBackground(Color.GRAY);
		
		JButton b = new JButton ("button 1");
		b.setBackground(Color.GRAY);
		
		JButton b2 = new JButton ("button 2");
		Color myNewColor = new Color (150, 100, 250, 100);
		b2.setBackground(myNewColor);
		
		JCheckBox cb1 = new JCheckBox("Do you LOVE bacon?");
		cb1.setBackground(Color.GRAY);
		
		JCheckBox cb2 = new JCheckBox("Do you LOVE java?");
		cb2.setBackground(Color.GRAY);
		

		JRadioButton rb1 = new JRadioButton("");
		JRadioButton rb2 = new JRadioButton("");
		JRadioButton rb3 = new JRadioButton("");
		JRadioButton rb4 = new JRadioButton("");
		JRadioButton rb5 = new JRadioButton("");
		JRadioButton rb6 = new JRadioButton("");
		JRadioButton rb7 = new JRadioButton("");
		JRadioButton rb8 = new JRadioButton("");
		JRadioButton rb9 = new JRadioButton("");
		JRadioButton rb10 = new JRadioButton("");
		JRadioButton rb11 = new JRadioButton("");
		JRadioButton rb12 = new JRadioButton("");
		JRadioButton rb13 = new JRadioButton("");
		JRadioButton rb14 = new JRadioButton("");
		JRadioButton rb15 = new JRadioButton("");
		JRadioButton rb16 = new JRadioButton("");
		JRadioButton rb17 = new JRadioButton("");
		JRadioButton rb18 = new JRadioButton("");
		
		
		
		GridBagConstraints gbc  = new GridBagConstraints();
		gbc.insets = new Insets(15, 15, 15, 15);
		//east 1x3
		//west 2x3
		//center 3x3
		
		p1.add(b);
		p1.add(b2);
		p3.add(cb1);
		p3.add(cb2);
		
		gbc.gridx = 0;
		gbc.gridy = 0;
		p5.add(rb1, gbc);
		gbc.gridx = 0;
		gbc.gridy = 1;
		p5.add(rb2, gbc);
		gbc.gridx = 0;
		gbc.gridy = 2;
		p5.add(rb3,gbc);
		gbc.gridx = 1;
		gbc.gridy = 0;
		p5.add(rb4, gbc);
		gbc.gridx = 1;
		gbc.gridy = 1;
		p5.add(rb5, gbc);
		gbc.gridx = 1;
		gbc.gridy = 2;
		p5.add(rb6,gbc);
		gbc.gridx = 2;
		gbc.gridy = 0;
		p5.add(rb7, gbc);
		gbc.gridx = 2;
		gbc.gridy = 1;
		p5.add(rb8, gbc);
		gbc.gridx = 2;
		gbc.gridy = 2;
		p5.add(rb9,gbc);
		
		gbc.gridx = 0;
		gbc.gridy = 0;
		p2.add(rb10, gbc);
		gbc.gridx = 0;
		gbc.gridy = 1;
		p2.add(rb11, gbc);
		gbc.gridx = 0;
		gbc.gridy = 2;
		p2.add(rb12,gbc);
		
		gbc.gridx = 0;
		gbc.gridy = 2;
		p4.add(rb13, gbc);
		gbc.gridx = 1;
		gbc.gridy = 2;
		p4.add(rb14, gbc);
		gbc.gridx = 0;
		gbc.gridy = 1;
		p4.add(rb15, gbc);
		gbc.gridx = 1;
		gbc.gridy = 1;
		p4.add(rb16, gbc);
		gbc.gridx = 0;
		gbc.gridy = 0;
		p4.add(rb17, gbc);
		gbc.gridx = 1;
		gbc.gridy = 0;
		p4.add(rb18, gbc);
		
		
		
		add(p1, BorderLayout.SOUTH);
		add(p2, BorderLayout.EAST);
		add(p5, BorderLayout.CENTER);
		add(p3, BorderLayout.NORTH);
		add(p4, BorderLayout.WEST);
		
		
		setVisible(true);
	}
	

}
