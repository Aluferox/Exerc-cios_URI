package helloworld;

import java.util.Scanner;

public class calculo_simples_1010 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		String pecaUm = scanner.nextLine();
		
		String[] peca1 = pecaUm.split(" ");
		
		String pecaDois = scanner.nextLine();
		
		String[] peca2 = pecaDois.split(" ");
		
		int valorP1 = Integer.parseInt(peca1[1]);
		float quantidadeP1 =  Float.parseFloat(peca1[2]);
		
		int valorP2 = Integer.parseInt(peca2[1]);
		float qunatidadeP2 = Float.parseFloat(peca2[2]);
		System.out.println("VALOR A PAGAR: R$ "+ (String.format("%.2f", ((valorP1 * quantidadeP1) + (valorP2 * qunatidadeP2)))));
	}
}
