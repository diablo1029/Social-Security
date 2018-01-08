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
	JButton addOneHome, addOneVisitor, resetButton;
	JButton addTwoHome, addThreeHome, addSixHome, minusOneHome;
	JButton addTwoVisitor, addThreeVisitor, addSixVisitor, minusOneVisitor;

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
		homeScore.setForeground(Color.BLUE);
		scorePanel.add(homeScore);
		
		visitorScore = new JLabel("" + visitorScoreAmount);
		visitorScore.setLocation(130,0);
		visitorScore.setSize(160, 30);
		visitorScore.setHorizontalAlignment(0);
		visitorScore.setForeground(Color.RED);
		scorePanel.add(visitorScore);
		
		buttonPanel = new JPanel();
		buttonPanel.setSize(320, 120);
		buttonPanel.setLocation(10, 90);
		buttonPanel.setLayout(null);
		totalGUI.add(buttonPanel);
		
		addOneHome = new JButton("Home Score +1");
		addOneHome.setLocation(0,0);
		addOneHome.setSize(160,30);
		addOneHome.addActionListener(this);
		addOneHome.setBackground(Color.BLUE);
		buttonPanel.add(addOneHome);
		
		addOneVisitor = new JButton("Visitor Score +1");
		addOneVisitor.setLocation(160,0);
		addOneVisitor.setSize(160,30);
		addOneVisitor.addActionListener(this);
		addOneVisitor.setBackground(Color.RED);
		buttonPanel.add(addOneVisitor);
		
		resetButton = new JButton("Start New Game");
		resetButton.setLocation(0,90);
		resetButton.setSize(320,30);
		resetButton.addActionListener(this);
		resetButton.setBackground(Color.GREEN);
		buttonPanel.add(resetButton);
		
		addTwoHome = new JButton("P");
		addTwoHome.setLocation(0,30);
		addTwoHome.setSize(80,30);
		addTwoHome.addActionListener(this);
		addTwoHome.setBackground(Color.BLUE);
		buttonPanel.add(addTwoHome);
		
		addThreeHome = new JButton("FG");
		addThreeHome.setLocation(80,30);
		addThreeHome.setSize(80,30);
		addThreeHome.addActionListener(this);
		addThreeHome.setBackground(Color.BLUE);
		buttonPanel.add(addThreeHome);
		
		addSixHome = new JButton("TD");
		addSixHome.setLocation(0,60);
		addSixHome.setSize(80,30);
		addSixHome.addActionListener(this);
		addSixHome.setBackground(Color.BLUE);
		buttonPanel.add(addSixHome);
		
		minusOneHome = new JButton("-1");
		minusOneHome.setLocation(80,60);
		minusOneHome.setSize(80,30);
		minusOneHome.addActionListener(this);
		minusOneHome.setBackground(Color.BLUE);
		buttonPanel.add(minusOneHome);
		
		addTwoVisitor = new JButton("P");
		addTwoVisitor.setLocation(160,30);
		addTwoVisitor.setSize(80,30);
		addTwoVisitor.addActionListener(this);
		addTwoVisitor.setBackground(Color.RED);
		buttonPanel.add(addTwoVisitor);
		
		addThreeVisitor = new JButton("FG");
		addThreeVisitor.setLocation(240,30);
		addThreeVisitor.setSize(80,30);
		addThreeVisitor.addActionListener(this);
		addThreeVisitor.setBackground(Color.RED);
		buttonPanel.add(addThreeVisitor);
		
		addSixVisitor = new JButton("TD");
		addSixVisitor.setLocation(160,60);
		addSixVisitor.setSize(80,30);
		addSixVisitor.addActionListener(this);
		addSixVisitor.setBackground(Color.RED);
		buttonPanel.add(addSixVisitor);
		
		minusOneVisitor = new JButton("-1");
		minusOneVisitor.setLocation(240,60);
		minusOneVisitor.setSize(80,30);
		minusOneVisitor.addActionListener(this);
		minusOneVisitor.setBackground(Color.RED);
		buttonPanel.add(minusOneVisitor);
	
		return totalGUI;
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource() == addOneHome) {
			homeScoreAmount = homeScoreAmount + 1;
			homeScore.setText("" + homeScoreAmount);
		}	else if (e.getSource() == addOneVisitor) {
			visitorScoreAmount = visitorScoreAmount + 1;
			visitorScore.setText("" + visitorScoreAmount);
		}	else if (e.getSource() == resetButton) {
			homeScoreAmount = 0;
			visitorScoreAmount = 0;
			homeScore.setText("" + homeScoreAmount);
			visitorScore.setText("" + visitorScoreAmount);
		}	else if (e.getSource() == addTwoVisitor) {
			visitorScoreAmount = visitorScoreAmount + 2;
			visitorScore.setText("" + visitorScoreAmount);
		}	else if (e.getSource() == addThreeVisitor) {
			visitorScoreAmount = visitorScoreAmount + 3;
			visitorScore.setText("" + visitorScoreAmount);
		}	else if (e.getSource() == addSixVisitor) {
			visitorScoreAmount = visitorScoreAmount + 6;
			visitorScore.setText("" + visitorScoreAmount);
		}	else if (e.getSource() == minusOneVisitor) {
			visitorScoreAmount = visitorScoreAmount - 1;
			visitorScore.setText("" + visitorScoreAmount);
		}	else if (e.getSource() == addTwoHome) {
			homeScoreAmount = homeScoreAmount + 2;
			homeScore.setText("" + homeScoreAmount);
		}	else if (e.getSource() == addThreeHome) {
			homeScoreAmount = homeScoreAmount + 3;
			homeScore.setText("" + homeScoreAmount);
		}	else if (e.getSource() == addSixHome) {
			homeScoreAmount = homeScoreAmount + 6;
			homeScore.setText("" + homeScoreAmount);
		}	else if (e.getSource() == minusOneHome) {
			homeScoreAmount = homeScoreAmount - 1;
			homeScore.setText("" + homeScoreAmount);
		}	
		
		
	}

}
