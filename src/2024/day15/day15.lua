local tools = require("src/tools")

local function move(map, current, yDiff, xDiff)
    local i, j = current[1], current[2]
    
    if map[i + yDiff][j + xDiff] == "#" then
        return false
    
    elseif map[i + yDiff][j + xDiff] == "." then
        map[i + yDiff][j + xDiff] = map[i][j]
        map[i][j] = "."
        pos = {pos[1] + yDiff, pos[2] + xDiff}
        return true
    
    elseif map[i + yDiff][j + xDiff] == "O" then
        if move(map, {i + yDiff, j + xDiff}, yDiff, xDiff) then
            map[i + yDiff][j + xDiff] = map[i][j]
            map[i][j] = "."
            return true
        else
            return false
        end

    end
end

-- Parse part 1
local file = io.open("src/day15/day15.txt", "rb")
local contents = file:read("a")
file:close()
contents = contents:gsub("\r\n", "\n")
local data = tools.split(contents, "\n\n")

local string_map = data[1]
local instructions = data[2]

local rows = tools.split(string_map, "\n")

local map = {}
for i, row in pairs(rows) do
    local current = {}
    for j = 1, #row do
        table.insert(current, string.sub(row, j, j))
        if string.sub(row, j, j) == "@" then
            pos = {i, j}
        end
    end
    table.insert(map, current)
end


-- Solve part 1
for i = 1, #instructions do
    if     string.sub(instructions, i, i) == "^" then move(map, pos, -1, 0)
    elseif string.sub(instructions, i, i) == "v" then move(map, pos, 1, 0)
    elseif string.sub(instructions, i, i) == "<" then move(map, pos, 0, -1)
    elseif string.sub(instructions, i, i) == ">" then move(map, pos, 0, 1)
    end
    --print("Move", string.sub(instructions, i, i) ..":")
    --for _, row in pairs(map) do
        --local current = ""
        --for _, c in pairs(row) do
        --    current = current .. c
        --end
        --print(current)
    --end
end

total = 0

for i, row in pairs(map) do
    for j, char in pairs(row) do
        if char == "O" then
            total = total + 100*(i - 1) + j - 1 -- Lua is 1-indexed
        end
    end
end

print(total)

-- Parse part 2

local map = {}
for i, row in pairs(rows) do
    local current = {}
    for j = 1, #row do
        local tile = string.sub(row, j, j)
        if tile == "." then
            table.insert(current, "..")
        elseif tile == "O" then
            table.insert(current, "[]")
        elseif tile == "#" then
            table.insert(current, "##")
        elseif tile == "@" then
            table.insert(current, "@.")
            pos = {i, j * 2 - 1}
        end
    end
    table.insert(map, current)
end

-- Recursive function for part 2
local function move2(map, current, yDiff, xDiff, tile)
    local i, j = current[1], current[2]
    
    if map[i + yDiff][j + xDiff] == "#" then
        return false
    elseif tile == "[" and map[i + yDiff][j + 1 + xDiff] == "#" then
        return false
    elseif tile == "]" and map[i + yDiff][j - 1 + xDiff] == "#" then
        return false
    
    elseif map[i + yDiff][j + xDiff] == "." then
        if tile == "[" and map[i + yDiff][j + 1 + xDiff] == "." then
            map[i + yDiff][j + xDiff] = map[i][j]
            map[i + yDiff][j + 1 + xDiff] = map[i][j + 1]
            map[i][j] = "."
            map[i][j+1] = "."
            pos = {pos[1] + yDiff, pos[2] + xDiff}
        elseif tile == "]" and map[i + yDiff][j - 1 + xDiff] == "." then
            map[i + yDiff][j + xDiff] = map[i][j]
            map[i + yDiff][j - 1 + xDiff] = map[i][j - 1]
            map[i][j] = "."
            map[i][j-1] = "."
            pos = {pos[1] + yDiff, pos[2] + xDiff}
        else
            map[i + yDiff][j + xDiff] = map[i][j]
            map[i][j] = "."
            pos = {pos[1] + yDiff, pos[2] + xDiff}  
        
            return true
        end
    elseif map[i + yDiff][j + xDiff] == "[" or map[i + yDiff][j + xDiff] == "]" then
        if move2(map,  {i + yDiff, j + xDiff},  yDiff,  xDiff,  map[i + yDiff][j + xDiff]) then
            if tile == "[" and map[i + yDiff][j + 1 + xDiff] == "." then
                map[i + yDiff][j + xDiff] = map[i][j]
                map[i + yDiff][j + 1 + xDiff] = map[i][j + 1]
                map[i][j] = "."
                map[i][j+1] = "."
                return true
            elseif tile == "]" and map[i + yDiff][j - 1 + xDiff] == "." then
                map[i + yDiff][j + xDiff] = map[i][j]
                map[i + yDiff][j - 1 + xDiff] = map[i][j - 1]
                map[i][j] = "."
                map[i][j-1] = "."
                return true
            elseif tile == "@" then
                map[i + yDiff][j + xDiff] = map[i][j]
                map[i][j] = "."
                return true
            else 
                return false
            end
        else
            return false
        end

    end
end

