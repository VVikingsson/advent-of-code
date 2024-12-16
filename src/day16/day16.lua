tools = require("src/tools")

local file = io.open("src/day16/day16.txt", "rb")
contents = file:read("a")

-- Parse into table
local maze = {}
local row = {}
for i = 1, #contents do
    if string.sub(contents, i, i) == "\n" then
        table.insert(maze, row)
        row = {}
    else
        table.insert(row, string.sub(contents, i, i))
    end
end

table.insert(maze, row)

function findStart(maze)
    for i, row in pairs(maze) do
        for j, tile in pairs(row) do
            if tile == "S" then
                start = {i, j}
            end
        end
    end
    return start
end

-- Debug print maze
for _, row in pairs(maze) do
    a = ""
    for _, char in pairs(row) do
        a = a .. char
    end
    print(a)
end



local function addQueue(queue, state)
    table.insert(queue, state)
end

local function shiftQueue(queue)
    item = queue[1]
    table.remove(queue, 1)
    print(item)
    return item
end

local function getNeighbors(maze, pos, dir, explored)
    local i = pos[1]
    local j = pos[2]
    local neighbors = {}

    local t = maze[i+1][j]
    if t ~= "#" and not tools.contains(explored, {i+1, j}) then
        table.insert(neighbors, {pos, t, dir})
    end
    t = maze[i-1][j]
    if t ~= "#" and not tools.contains(explored, {i-1, j}) then
        table.insert(neighbors, {pos, t, dir})
    end
    t = maze[i][j+1]
    if t ~= "#" and not tools.contains(explored, {i, j+1}) then
        table.insert(neighbors, {pos, t, dir})
    end
    t = maze[i][j-1]
    if t ~= "#" and not tools.contains(explored, {i, j-1}) then
        table.insert(neighbors, {pos, t, dir})
    end
    return neighbors
end

local start = findStart(maze)

-- explored states: from, to, dir
local explored = {}
-- table with anonymous functions mapping a state to another and returning the cost of its step
local costs = {}
-- Queue: from, to, dir (positions)
local queue = {}
local found_goal = false


local chance_for_better = true
local goal_cost = math.huge  -- Initialize goal_cost to be infinite
local first_iteration = true
-- Temporary values needed to go through the loop
local to = start
local new_dir = {0, 1}
while first_iteration or #queue > 0 do

    print("Iteration")
    local neighbors = getNeighbors(maze, to, new_dir, explored) -- adds a table, should add individual elements
    local cost = 0
    
    if not first_iteration then
        local state = shiftQueue(queue)
        print("HERE:", tools.dump(state))
        local from = state[1]
        local to = state[2]
        local current_dir = state[3]
        print(to, from[1], from[2])
        local new_dir = {to[1] - from[1], to[2] - from[2]}
        
        if new_dir == current_dir then
            cost = 1 + costs[from]
            costs[to] = cost
        else
            cost = 90 + costs[from]
            costs[to] = cost
        end

        if maze[to[1]][to[2]] == "E" then
            if cost < goal_cost then
                goal_cost = cost
            end
        end
    end 

    table.insert(explored, {from, to, current_dir})

    if cost < goal_cost then
        for i, nb in pairs(neighbors) do
            addQueue(queue, nb)
            print("Added neighbor to queue")
    end
    first_iteration = false

    
end

print(goal_cost)

end