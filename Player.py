class Player:
    def __init__(self, apiResponse):
        self.id = apiResponse["id"]
        self.username = apiResponse["username"]
        self.displayName = apiResponse["displayName"]
        self.type = apiResponse["type"]
        self.build = apiResponse["build"]
        self.country = apiResponse["country"]
        self.status = apiResponse["status"]
        self.exp = apiResponse["exp"]
        self.ehp = apiResponse["ehp"]
        self.ehb = apiResponse["ehb"]
        self.ttm = apiResponse["ttm"]
        self.tt200m = apiResponse["tt200m"]
        self.registeredAt = apiResponse["registeredAt"]
        self.updatedAt = apiResponse["updatedAt"]
        self.lastChangedAt = apiResponse["lastChangedAt"]
        self.lastImportedAt = apiResponse["lastImportedAt"]

        self.score = self.ehp + (self.ehb * 2)

    def __str__(self):
        return f"{self.displayName} | score={self.score}"

    def __repr__(self):
        return f"{self.displayName} | EHP={self.ehp}, EHB={self.ehb}"

    def __lt__(self, other):
        return self.score < other.score
