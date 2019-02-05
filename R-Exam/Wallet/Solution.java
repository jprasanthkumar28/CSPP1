import java.util.Scanner;

public class Solution {
	public static void main(String args[]) {

		Scanner s = new Scanner(System.in);
		String name = s.nextLine();
		int c = 0;
		int num = Integer.parseInt(s.nextLine());
		User u = new User(num);
		u.name = name;
		for (int i = 0; i < num; i++) {
			u.addWallet(s.nextLine());

		}
		c = 0;
		int flag = 0;
		while (s.hasNext()) {
			String operation = s.nextLine();
			if (operation.equals("quit")) {
				System.out.println("Thank you");
				break;
			}
			switch (operation) {
				//Please complete the code for credit,debit,transfer and balance operations 
			case "credit":
				
				break;
			case "transfer":
				
				break;

			case "debit":
				
				break;
			case "balance":
				
				break;

			}
		}
	}
}
