import java.util.*;
public class test{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int sub = sc.nextInt();
		int totlikes = 0;
		int totviews = 0;
		int amtpaid = 0;
		if(n<3){
			System.out.println("Invalid");
		}
		else{
			for (int i = 0; i < n; i++) {
				totviews += sc.nextInt();
				totlikes += sc.nextInt();
			}
			if(totviews<totlikes){
				System.out.println("Invalid");
			}
			else{
				if(totlikes>=100 && totviews>=100 && sub>=100){
					amtpaid +=1;
					totlikes -= 100;
					totviews -= 100;
					sub -= 100;
					int like5 = totlikes/50;
					int view5 = totviews/50;
					int sub5 = sub/50;
					amtpaid += (like5 * 5) + (view5 * 5) + (sub5 * 5);
					System.out.println(amtpaid*74.80);
				}
				else{
					System.out.println(0);
				}
				
			}
		}
		sc.close();
	}
}