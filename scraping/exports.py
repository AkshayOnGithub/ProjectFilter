from pathlib import Path
from typing import Iterable

import pandas as pd
import yaml

from scraping.scrapers import Scraper, QA


def export_yml(scraper_name: str, scraped: Iterable[QA], target_folder: Path):
    filename = scraper_name + ".yml"
    yml_file = target_folder / filename
    with open(yml_file, "w") as f:
        items = []
        for i in scraped:
            # items.append({"question": i.question, "answer": i.answer})
            items.append(i.question)
            items.append(i.answer)
        yaml.dump(items, f, sort_keys=False)


def export_csv(scraper_name: str, scraped: Iterable[QA], target_folder: Path, sep=";"):
    filename = scraper_name + ".csv"
    csv_file = target_folder / filename
    questions = [qa.question for qa in scraped]
    answers = [qa.answer for qa in scraped]
    df = pd.DataFrame({"question": questions, "answer": answers})
    df.to_csv(csv_file, sep=sep, index=False, header=True)


if __name__ == "__main__":
    target_dir = Path("/Users/jlinho/Desktop/gr")
    scrapers = Scraper.all()
    for name, scraper in scrapers.items():
        scraped = scraper.scrape()
        export_yml(name, scraped, target_dir)
        export_csv(name, scraped, target_dir)
