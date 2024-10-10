import java.util.*;
public class simplesieve{
    public int[] simpsieve(int limit){
        boolean[] isprime = new boolean[limit];
        Arrays.fill(isprime, true);

        for(int i = 0; i*i < limit; i++){
            if(isprime[i]==true){
                for(int j = i*i; j < limit; j++){
                    isprime[j]=false;
                }
            }
        }
        int count=0;
        int[] prime = new int[limit];
        for(int i=0; i<limit; i++){
            if(isprime[i] == true){
                prime[count++]=i;
            }
        }
        return prime;
    }
}
