public class Cadenas{
    public static void main (String[] args){
        String saludo = "¡Hola mundo yo soy programador Java!";
        int longitud= saludo.length();
        char myChar=saludo.charAt(2);
        boolean stringVacio = saludo.isEmpty();
        boolean containsString = saludo.contains("prog");
        String substring = saludo.substring(2,7);
        String newSting =saludo.replace("o","5");
        System.out.println(saludo+"\n"+longitud+"\n"+myChar+"\n"+stringVacio+"\n"+containsString+"\n"+substring+"\n"+newSting+"\n\n");
        
        int edad=25; //variable entera
        System.out.println("Mi edad es: "+ edad);

        float altura= 1.70f; //variable de coma flotante
        System.out.println("Mi altura es: "+ altura);

        double valorDePi=3.141597843485821; // variable de coma flotante para valores con muchos decimales
        System.out.println("El valor de Pi es: "+ valorDePi);

        long distanciaAlSol = 1234567890123456789L; //variable similar a la de tipo entero, pero para numeros mucho más grandes
        System.out.println("La distancia al sol es: "+ distanciaAlSol);
        
        boolean IsDay = false;
        System.out.println("¿Es de dia?: " + IsDay);
        
        char miInicial='y';
        System.out.println("Mi primer caracter es: " + miInicial);

        //camelCase
    }
}
