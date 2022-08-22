import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public


class Main {
public static void main(String[] args) throws IOException {
InputStreamReader isr = new InputStreamReader(System.in );
BufferedReader br = new BufferedReader(isr);
int n;
do{
int corridas = 0;
do{
n = Integer.parseInt(br.readLine());
}


while ((n < 0) | | (n > 100000));
int
marrecos = n;
while (marrecos > 1){
if (marrecos % 3 == 0){
corridas += marrecos / 3;
marrecos /= 3;
} else {
corridas += (marrecos / 3) + 1;
marrecos = (marrecos / 3) + 1;
}

}
if (marrecos > 0){
System.out.println(corridas);
}
}while (n != 0);
}
}