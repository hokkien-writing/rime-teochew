local function add_space(str)
    return str.." "
end


local function add_space_if_not_end_with_hyphen(str)
  if string.sub(str, -1) ~= "-" then
    return str .. " "
  else
    return str
  end
end

function puj_spacer(input, env)
    for cand in input:iter() do
        cand = cand:to_shadow_candidate(cand.type, add_space(cand.text), cand.comment)
        yield(cand)
    end
end


return puj_spacer
