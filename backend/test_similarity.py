from fusion.similarity_matcher import SimilarityMatcher

matcher = SimilarityMatcher()

root_causes = [

"WAL segment corruption caused by a failing NVMe SSD with degrading sectors on the primary database server",

"WAL segment corruption caused by failing NVMe SSD",

"Possible WAL related failure"

]

print(matcher.match(root_causes))
