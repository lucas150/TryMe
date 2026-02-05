

const app = express();

app.use(express.json());

app.get("/", (req, res) => {
  res.send("Backend running");
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
function express() {
    throw new Error("Function not implemented.");
}

