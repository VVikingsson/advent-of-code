WIDTH = 101
HEIGHT = 103

local file = io.open("inputs/day14.txt", "rb")
contents = file:read("a")
file:close()

local robots = {}
local i = 1
local j = 0
for match in string.gmatch(contents, "%-?%d+") do
    print(i, match)
    if (i - 1) % 4 == 0 then
        j = j + 1
        robots[j] = {}
        robots[j]["pos"] = {tonumber(match)}

    elseif (i - 1) % 4 == 1 then
        table.insert(robots[j]["pos"], 2, tonumber(match))

    elseif (i - 1) % 4 == 2 then
        robots[j]["vel"] = {tonumber(match)}
    
    elseif (i - 1) % 4 == 3 then
        table.insert(robots[j]["vel"], 2, tonumber(match))
    
    end
    i = i + 1
end
print("Length of robots", #robots)
for i = 1, #robots do
    print("Trying to print table")
    print(i)
    print(robots[i]["pos"][1], robots[i]["pos"][2])
    print(robots[i]["vel"][1], robots[i]["vel"][2])
end

local finalPositions = {}

for _, robot in pairs(robots) do
    local totalX = robot["pos"][1] + 100 * robot["vel"][1]
    local totalY = robot["pos"][2] + 100 * robot["vel"][2]

    local finalX = totalX % WIDTH
    local finalY = totalY % HEIGHT
    local quadrant = ""

    if finalY > math.floor(HEIGHT / 2) then
        quadrant = quadrant .. "bot"
    elseif finalY < math.floor(HEIGHT / 2) then
        quadrant = quadrant .. "top" end

    if finalX > math.floor(WIDTH / 2) then
        quadrant = quadrant .. "right"
    elseif finalX < math.floor(WIDTH / 2) then
        quadrant = quadrant .. "left" end

    if finalPositions[quadrant] then
        finalPositions[quadrant] = finalPositions[quadrant] + 1
    else
        finalPositions[quadrant] = 1
    end

end

for q, count in pairs(finalPositions) do
    print(q, count)
end

local result = finalPositions["topright"] * finalPositions["botright"] * finalPositions["topleft"] * finalPositions["botleft"]

print(result)



