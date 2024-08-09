-- List all bands with Glam rock as their main style, ranked by their longevity
-- Lifespan is calculated as the difference between 2022 and the year the band was formed,
-- or the year they split if they have split.

SELECT band_name,
       CASE
           WHEN split IS NOT NULL THEN split - formed
           ELSE 2022 - formed
       END AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', style)
ORDER BY lifespan DESC, band_name ASC;
