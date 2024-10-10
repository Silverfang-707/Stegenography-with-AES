import java.util.Scanner;
public class Solution {
    public static void main(String[] args) {
        simplesieve ss = new simplesieve();
        segmentedsieve segm = new segmentedsieve();
        Scanner sc = new Scanner(System.in);
        System.out.print("From: ");
        int low = sc.nextInt();
        System.out.print("To:");
        int high = sc.nextInt();
        sc.close();
        int n = 100000;
        int[] primes = ss.simpsieve(n);
        int[] primesInRange = segm.segmentedSieve(primes, low, high);
        for (int prime : primesInRange) {
            System.out.println(prime);
        }
    }
}

