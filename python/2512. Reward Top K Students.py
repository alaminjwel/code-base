class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        ranking = {item: 0 for item in student_id}

        for i in range(len(report)):
            tokens = report[i].split(' ')
            points = 0
            for token in tokens:
                if token in positive_feedback:
                    points += 3
                elif token in negative_feedback:
                    points -= 1
            ranking[student_id[i]] = points
        sortedRanking = sorted(ranking.items(), key=lambda x: (-x[1], x[0]))[:k]
        return [x[0] for x in sortedRanking]