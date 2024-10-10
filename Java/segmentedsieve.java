public class segmentedsieve {
    public int[] segmentedSieve(int[] primes, int low, int high) {
        int[] primesInRange = new int[high - low + 1];
        int count = 0;
        for (int prime : primes) {
            if (prime >= low && prime <= high) {
                primesInRange[count++] = prime;
            }
        }
        return primesInRange;
    }
}

