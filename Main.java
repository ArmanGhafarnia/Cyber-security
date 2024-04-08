import java.util.concurrent.*;

public class Main {

    static int len = 0;
    static int num = 433;
    static long one_time = 100000000;
    static long zero_time = 50000000;
    static volatile boolean wait = false;
    static long error = 20000000;
    static long start_send;
    static long end_recive;


    public static void main(String[] args) {
        send Send = new send();
        recieve Receive = new recieve();

        Send.start();
        Receive.start();


    }

    static class send extends Thread {
        @Override
        public void run() {
            String bi_num = Integer.toBinaryString(num);
            System.out.println(bi_num + " (sent)");
            len = bi_num.length();
            start_send = System.nanoTime();
            for (int i = 0; i < len; i++) {
                char k = bi_num.charAt(i);
                if (k == '0') {
                    wait = true;
                    try {
                        TimeUnit.NANOSECONDS.sleep(zero_time);
                    } catch (Exception e) {}
                    wait = false;
                } else {
                    wait = true;
                    try {
                        TimeUnit.NANOSECONDS.sleep(one_time);
                    } catch (Exception e) {}
                    wait = false;
                }
            }

        }
    }

    static class recieve extends Thread {
        @Override
        public void run() {
            String hole_num = "";
            while (hole_num.length() < len + 1) {
                long first = System.nanoTime();
                while (wait) {}
                long second = System.nanoTime();
                long doing = second - first;
                char message;
                if (doing < (zero_time + error)) {
                    message = '0';
                } else {
                    message = '1';
                }
                hole_num = hole_num + message;
            }
            end_recive = System.nanoTime();
            int hole_num2 = Integer.parseInt(hole_num, 2);
            System.out.println(hole_num2 + " (received)");
            System.out.println(((double) (end_recive - start_send) /1000000000) / len + " (speed)");
        }
    }



}
