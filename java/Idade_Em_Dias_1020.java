package helloworld;
import java.util.Scanner;

public class Idade_Em_Dias_1020 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		String entrada = scanner.next();
		int idade = Integer.parseInt(entrada);
		
		int anos = idade / 365;
		
		int meses = (idade % 365) / 30;
		
		int dias = (idade%365)%30;
		
		System.out.println(anos + " ano(s)");
		System.out.println(meses+ " mes(es)");
		System.out.println(dias + " dia(s)");
	}
}
