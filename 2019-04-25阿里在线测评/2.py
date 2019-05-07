# n = int(input())
#
# def lift(n):
#       if n <= 2:
#             return n
#       else:
#             return lift(n-1) + lift(n-2)
# print(lift(n))


# public class Main {
#
#     public static void main(String[] args) {
# 	    // write your code here
# 	    for (int i=2;i<1001; ++i ){
# 	          int res = 0;
# 	          for (int j=2; j< i/2 + 1; ++j){
# 	                if (i%j == 0){
# 	                      res += j;
# 	                }
# 	          }
# 	          res += 1;
# 	          if (res == i){
# 	                System.out.println(res);
# 	          }
# 	    }
#
#     }
# }


# import java.util.Scanner;
#
# public class qu2 {
#
# public static void main(String[] args) {
# // write your code here
# Scanner sc = new Scanner(System.in );
# int n = sc.nextInt();
# int res = help(n);
# System.out.println(res);
# }
#
# static int help(int n) {
# // write your code here
# if (n <= 2){
#
#
# return n;
# }
# else {
# return help(n - 1) + help(n - 2);
# }
# }
# }
