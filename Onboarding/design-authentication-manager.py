class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.life = timeToLive
        self.tokens = {}
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.life + self.tokens[tokenId] >  currentTime:
            self.tokens[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        limit = currentTime - self.life
        return  len([time for time in self.tokens.values() if time > limit])


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)