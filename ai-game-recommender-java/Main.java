import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Recommender recommender = new Recommender();

        System.out.println("AI Game Recommender");
        System.out.println("-------------------");

        System.out.print("Enter a game you like: ");
        String game = scanner.nextLine();

        List<Game> recommendations = recommender.recommend(game);

        if (recommendations.isEmpty()) {
            System.out.println("Sorry, no recommendations found.");
        } else {
            System.out.println("\nRecommended games:");

            for (Game g : recommendations) {
                System.out.println("- " + g.getName());
            }
        }

        scanner.close();
    }
}