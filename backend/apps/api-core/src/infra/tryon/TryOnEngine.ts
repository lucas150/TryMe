export interface TryOnEngine {
  run(input: {
    avatarImagePath: string;
    garmentImagePath: string;
  }): Promise<{ outputImagePath: string }>;
}
