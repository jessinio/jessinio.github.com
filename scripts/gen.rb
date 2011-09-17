if ARGV.length == 0
  p 'please specify the name of your blog. e.g. write-a-ruby-script'
else
  name = Date.today.to_s + '-' + ARGV.to_s + '.textile'
  name_with_path = '../_posts/' + name
  template = [
    '---',
    'layout: post',
    'title: ',
    'categories: refactoring code',
    '---',
    '',
    '',
    '<pre class="terminal"><code></code></pre>',
    '<pre><code></code></pre>',
    '',
    '']

  blog = File.new(name_with_path, 'w')
  template.each { |line| blog.puts line }
  
  p 'blog created at ' + name_with_path
end


