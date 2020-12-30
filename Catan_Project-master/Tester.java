public class Tester {
    public static void main(String[] args) {
        Player player1 = new Player();
        player1.setResources("ore", 10);

        Player player2 = new Player();
        player2.setResources("lumber", 500);
        System.out.println(" player 2: " + player2.toString());
        System.out.println("player 1: " + player1.toString());

        player1.trade_player(player2, "ore", "lumber");
        System.out.println(" player 2: " + player2.toString());
        System.out.println("player 1: " + player1.toString());

    }
}
