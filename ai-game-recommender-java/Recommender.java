import java.util.ArrayList;
import java.util.List;

public class Recommender {

    private List<Game> games;

    public Recommender() {
        games = new ArrayList<>();

        games.add(new Game("Minecraft", "Sandbox"));
        games.add(new Game("Terraria", "Sandbox"));
        games.add(new Game("Stardew Valley", "Simulation"));
        games.add(new Game("Roblox", "Sandbox"));
        games.add(new Game("Call of Duty", "Shooter"));
        games.add(new Game("Apex Legends", "Shooter"));
        games.add(new Game("Valorant", "Shooter"));
        games.add(new Game("The Sims", "Simulation"));
    }

    public List<Game> recommend(String gameName) {

        String genre = null;

        for (Game g : games) {
            if (g.getName().equalsIgnoreCase(gameName)) {
                genre = g.getGenre();
                break;
            }
        }

        List<Game> recommendations = new ArrayList<>();

        if (genre != null) {
            for (Game g : games) {
                if (g.getGenre().equalsIgnoreCase(genre)
                        && !g.getName().equalsIgnoreCase(gameName)) {
                    recommendations.add(g);
                }
            }
        }

        return recommendations;
    }
}