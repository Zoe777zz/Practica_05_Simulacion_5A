import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Locale;

public class GeneradorJava {
    // Parametros iguales a los de Python.
    static final long MULTIPLICADOR = 1664525L;
    static final long INCREMENTO = 1013904223L;
    static final long MODULO = 4294967296L;
    static final int CANTIDAD = 10000;

    static void generar(long semilla, String nombreArchivo) throws IOException {
        Files.createDirectories(Path.of("salidas"));
        try (BufferedWriter archivo = Files.newBufferedWriter(
                Path.of("salidas", nombreArchivo), StandardCharsets.UTF_8)) {
            archivo.write("n,Xn,Un\n");
            long numero = semilla;
            for (int n = 1; n <= CANTIDAD; n++) {
                numero = (MULTIPLICADOR * numero + INCREMENTO) % MODULO;
                double valor = (double) numero / MODULO;
                archivo.write(String.format(Locale.US, "%d,%d,%.10f%n", n, numero, valor));
                if (n <= 20 && semilla == 12345L) {
                    System.out.printf(Locale.US, "%-3d %12d   %.10f%n", n, numero, valor);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.out.println("JAVA - Primeros 20 valores (semilla 12345)");
        System.out.println("n       Xn            Un");
        generar(12345L, "secuencia_java.csv");
        generar(54321L, "secuencia_java_otra_semilla.csv");
        System.out.println("\nSe generaron 10 000 valores por semilla.");
        System.out.println("CSV guardados en la carpeta salidas/.");
    }
}
