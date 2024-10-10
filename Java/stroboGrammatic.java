import java.util.*;
public class stroboGrammatic {
    public static boolean isstrobogrammatic (String num){
        Map<Character, Character> map = new HashMap<Character, Character>();
        map.put('6','9');
        map.put('9','6');
        map.put('0','0');
        map.put('1','1');
        map.put('8','8');
        int i = 0, r=num.length()-1;
        while(i<r) {
            if(!map.containsKey(num.charAt(i))){
                return false;
            }
            if(map.get(num.charAt(i))!=num.charAt(r)){
                return false;
            }
            i++;
            r--;
        }
        return true;
    }
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number: ");
        String number = scanner.next();
        scanner.close();
        System.out.println(isstrobogrammatic(number));
    }
}
