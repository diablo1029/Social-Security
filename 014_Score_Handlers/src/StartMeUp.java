import javax.swing.SwingUtilities;
public class StartMeUp {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		GiveMeGUI myGUI = new GiveMeGUI();
		
		SwingUtilities.invokeLater(new Runnable() {
			public void run() {
				myGUI.createAndShowGUI();
			}
		});
	}

}
