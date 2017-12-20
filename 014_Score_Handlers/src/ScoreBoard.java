import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.Color;
import java.awt.Container;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class ScoreBoard implements ActionListener {
	// example ...Scoreboard extends JFrame implements ActionListener GOOD
	// example ...Scoreboard extends JFrame implements ActionListener, AnotherOne
	// GOOD
	// example ...Scoreboard extends JFrame,JPanel implements ActionListener BAD

	// extends means inherit - use all vars and methods of the superclass
	// implements means you must use an "interface"

	int homeScoreAmount = 0;
	int visitorScoreAmount = 0;

	JPanel titlePanel, scorePanel, buttonPanel;
	JLabel homeLabel, visitorLabel, homeScore, visitorScore;
	JButton homeButton, visitorButton, resetButton;

	public Container createContentPane() {

		JPanel totalGUI = new JPanel();
		totalGUI.setSize(320, 300);
		totalGUI.setBackground(Color.YELLOW);
		totalGUI.setLayout(null);

		JPanel titlePanel = new JPanel();
		titlePanel.setLayout(null);
		titlePanel.setLocation(10, 10);
		titlePanel.setSize(320, 30);
		totalGUI.add(titlePanel);

		homeLabel = new JLabel("home Team");
		homeLabel.setLocation(0, 0);
		homeLabel.setSize(160, 30);
		homeLabel.setHorizontalAlignment(0);
		homeLabel.setForeground(Color.BLUE);
		titlePanel.add(homeLabel);
		
		visitorLabel = new JLabel("visitor Team");
		visitorLabel.setLocation(160, 0);
		visitorLabel.setSize(160, 30);
		visitorLabel.setHorizontalAlignment(0);
		visitorLabel.setForeground(Color.RED);
		titlePanel.add(visitorLabel);
		
		scorePanel = new JPanel();
		scorePanel.setSize(320, 30);
		scorePanel.setLocation(10, 50);
		scorePanel.setLayout(null);
		totalGUI.add(scorePanel);
		
		homeScore = new JLabel("" + homeScoreAmount);
		homeScore.setLocation(0,0);
		homeScore.setSize(160, 30);
		homeScore.setHorizontalAlignment(0);
		homeScore.setBackground(Color.BLUE);
		scorePanel.add(homeScore);
		
		visitorScore = new JLabel("" + visitorScoreAmount);
		visitorScore.setLocation(130,0);
		visitorScore.setSize(160, 30);
		visitorScore.setHorizontalAlignment(0);
		visitorScore.setBackground(Color.RED);
		scorePanel.add(visitorScore);
		
		buttonPanel = new JPanel();
		buttonPanel.setSize(320, 100);
		buttonPanel.setLocation(10, 90);
		buttonPanel.setLayout(null);
		totalGUI.add(buttonPanel);
		
		homeButton = new JButton("Home Score +1");
		homeButton.setLocation(0,0);
		homeButton.setSize(160,30);
		homeButton.addActionListener(this);
		homeButton.setBackground(Color.BLUE);
		buttonPanel.add(homeButton);
		
		visitorButton = new JButton("Visitor Score +1");
		visitorButton.setLocation(160,0);
		visitorButton.setSize(160,30);
		visitorButton.addActionListener(this);
		visitorButton.setBackground(Color.RED);
		buttonPanel.add(visitorButton);
		
		resetButton = new JButton("Start New Game");
		resetButton.setLocation(0,30);
		resetButton.setSize(320,30);
		resetButton.addActionListener(this);
		resetButton.setBackground(Color.GREEN);
		buttonPanel.add(resetButton);
	
		return totalGUI;
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource() == homeButton) {
			homeScoreAmount = homeScoreAmount + 1;
			homeScore.setText("" + homeScoreAmount);
		}	else if (e.getSource() == visitorButton) {
			visitorScoreAmount = visitorScoreAmount + 1;
			visitorScore.setText("" + visitorScoreAmount);
		}	else if (e.getSource() == resetButton) {
			homeScoreAmount = 0;
			visitorScoreAmount = 0;
			homeScore.setText("" + homeScoreAmount);
			visitorScore.setText("" + visitorScoreAmount);
		}
		
		
	}

}
