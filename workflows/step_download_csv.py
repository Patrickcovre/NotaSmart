def step_download_csv(output_text: str):
    csv_path = os.path.join(os.path.dirname(__file__), "data.csv")
    with open(csv_path, "w", encoding="utf-8") as f:
        f.write(output_text)
