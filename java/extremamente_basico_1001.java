package helloworld;
import java.util.Scanner;

public class extremamente_basico_1001 {
	 public static void main(String[] args) {
		 Scanner scanner = new Scanner(System.in);
		 String a = scanner.nextLine();
		 String b = scanner.nextLine();
		 
		 int soma = Integer.parseInt(a) + Integer.parseInt(b);
		 System.out.println("X = " + soma);
	 }
}
