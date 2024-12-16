tools = {}

function tools.strip(str)
    return str:match("^%s*(.-)%s*$")
end

function tools.split(str, splitter)
    result = {""}
    current = 1
    i = 1
    while i <= #str do
        if string.sub(str, i, i + #splitter - 1) == splitter then
            current = current + 1
            result[current] = ""
            i = i + #splitter - 1
        else
            result[current] = result[current] .. string.sub(str, i, i)
        end
        i = i + 1
    end
    return result
end

function tools.contains(list, element)
    for i, e in pairs(list) do
        if e == element then return true end
    end
    return false
end

return tools