from rapidfuzz import fuzz


class SimilarityMatcher:

    def match(self, values, threshold=65):

        unique = []

        for value in values:

            duplicate = False

            for existing in unique:

                score = max(
                    fuzz.token_sort_ratio(value.lower(), existing.lower()),
                    fuzz.partial_ratio(value.lower(), existing.lower()),
                    fuzz.token_set_ratio(value.lower(), existing.lower()),
                )

                if score >= threshold:
                    duplicate = True
                    break

            if not duplicate:
                unique.append(value)

        return unique
