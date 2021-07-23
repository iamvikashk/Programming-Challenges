SELECT c.contest_id, c.hacker_id, c.name, sum(total_submissions), sum(total_accepted_submissions), sum(total_views), sum(total_unique_views)
FROM contests c
LEFT JOIN colleges c1
    ON c.contest_id = c1.contest_id
LEFT JOIN challenges c2
    ON c1.college_id = c2.college_id
LEFT JOIN (SELECT challenge_id, Sum(total_views) AS total_views, Sum(total_unique_views) AS total_unique_views FROM view_stats GROUP BY challenge_id) AS vs 
    ON c2.challenge_id = vs.challenge_id
LEFT JOIN (SELECT challenge_id, Sum(total_submissions) AS total_submissions, Sum(total_accepted_submissions) AS total_accepted_submissions FROM submission_stats GROUP BY challenge_id) AS ss 
    ON c2.challenge_id = ss.challenge_id
GROUP BY c.contest_id, c.hacker_id, c.name
HAVING sum(total_submissions) > 0 and sum(total_accepted_submissions) > 0 and sum(total_views) > 0 and sum(total_unique_views) > 0
ORDER BY c.contest_id