-- Rank country origins of bands by the number of (non-unique) fans
-- This query ranks countries based on the total number of fans of bands originating from those countries.

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
