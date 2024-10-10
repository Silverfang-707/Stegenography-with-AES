import okhttp3.*;

import java.io.IOException;
import java.util.Scanner;

public class Main {
    private static final String BASE_URL = "https://integrate.api.nvidia.com/v1";
    private static final String API_KEY = "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"; // replace with your API key

    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient();

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter content:");
        String content = scanner.nextLine();

        MediaType mediaType = MediaType.parse("application/json");
        String jsonBody = String.format("{\n  \"model\":\"google/gemma-7b\",\n  \"messages\":[{\"role\":\"user\",\"content\":\"%s\"}],\n  \"temperature\":0.5,\n  \"top_p\":1,\n  \"max_tokens\":1024\n}", content);
        RequestBody body = RequestBody.create(mediaType, jsonBody);
        Request request = new Request.Builder()
                .url(BASE_URL + "/chat/completions")
                .post(body)
                .addHeader("content-type", "application/json")
                .addHeader("authorization", "Bearer " + API_KEY)
                .build();

        try {
            Response response = client.newCall(request).execute();
            System.out.println(response.body().string());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
