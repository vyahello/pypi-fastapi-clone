from typing import List, Optional


class Package:
    def __init__(  # noqa: CFQ002
        self,
        package_name: str,
        summary: str,
        description: str,
        home_page: str,
        lic: str,
        author_name: str,
        maintainers: Optional[List[str]] = None,
    ) -> None:
        if not maintainers:
            self.maintainers: List[str] = []
        self.package_name = package_name
        self.id = package_name
        self.summary = summary
        self.description = description
        self.home_page = home_page
        self.license = lic
        self.author_name = author_name
        self.maintainers = maintainers  # type: ignore
