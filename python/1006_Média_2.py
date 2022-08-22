import java.io.IOException;
import java.util.Scanner;
/ **
*IMPORTANT:
*O
nome
da
classe
deve
ser
"Main"
para
que
a
sua
solução
execute
*Class
name
must
be
"Main"
for your solution to execute
*El
nombre
de
la
clase
debe
ser
"Main"
para
que
su
solución
ejecutar
* /
public


class Main {

public static void main(String[] args) throws IOException {
Scanner sc = new Scanner(System.in );
/ **
* Escreva a sua solução aqui
* Code your solution here
* Escriba su solución aquí
* /

double A = sc.nextDouble();
double B = sc.nextDouble();
double C = sc.nextDouble();
double MEDIA = ((A * 2) + (B * 3) + (C * 5)) / 10;
System.out.printf("MEDIA = %.1f\n", MEDIA);

}

}