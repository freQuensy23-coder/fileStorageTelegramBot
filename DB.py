from collections import namedtuple
import asyncio


class DB:
    def __init__(self):
        self._files = []

    def save_file(self, tags: list, file_id: str):
        """Сохраняет данные о фалйе в бд"""
        structure_file_data = namedtuple("file_data", ["tags", "file_id"])
        file_data = structure_file_data(tags=tags, file_id=file_id)
        self._files.append(file_data)

    async def get_files(self, tags):
        """Ищет файлы с данными тегами"""
        for i, tag in enumerate(tags):  # Все теги - слова в нижнем регистре.
            tags[i] = tag.lower()

        result = []
        for searching_tag in tags:
            for file in self._files:
                for file_tag in file.tags:
                    if file_tag == searching_tag:
                        result.append(file)
                        break  # TODO Оптимизировать брэйком что бы переходили к следующему файлу
        return result
