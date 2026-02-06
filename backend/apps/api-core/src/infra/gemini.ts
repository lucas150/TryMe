import { GoogleGenerativeAI } from "@google/generative-ai";

const apiKey = process.env.GEMINI_API_KEY;

if (!apiKey) {
  throw new Error("GEMINI_API_KEY is not set");
}

export const genAI = new GoogleGenerativeAI(apiKey);

export const nanoBananaModel = genAI.getGenerativeModel({
  model: "gemini-2.5-flash-image",
});
