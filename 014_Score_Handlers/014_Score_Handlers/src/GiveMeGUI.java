import javax.swing.JFrame;
public class GiveMeGUI {
	void createAndShowGUI() {
		JFrame.setDefaultLookAndFeelDecorated(true);
		JFrame frame = new JFrame("Score Board");
		
		ScoreBoard demo = new ScoreBoard();
		frame.setContentPane(demo.createContentPane());
		
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setLocationRelativeTo(null);
		frame.setSize(350, 300);
		frame.setVisible(true);
	}
}
