import React, { useState, useEffect } from 'react';
import PostList from '../components/PostList';
import CategoryFilter from '../components/CategoryFilter';
import { getPosts } from '../services/api';

const PostListPage = () => {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedCategory, setSelectedCategory] = useState('All');

  useEffect(() => {
    const fetchPosts = async () => {
      setLoading(true);
      try {
        const data = await getPosts(selectedCategory === 'All' ? null : selectedCategory);
        setPosts(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchPosts();
  }, [selectedCategory]);

  return (
    <div className="max-w-5xl mx-auto">
      <div className="flex flex-col sm:flex-row justify-between items-center mb-8 gap-4">
        <h1 className="text-4xl font-extrabold tracking-tight text-gray-900">Blog Posts</h1>
        <CategoryFilter onCategoryChange={setSelectedCategory} />
      </div>
      {loading && <div className="text-gray-500 text-center py-8">Loading...</div>}
      {error && <div className="text-red-500 text-center py-8">Error: {error}</div>}
      {!loading && !error && <PostList posts={posts} />}
    </div>
  );
};

export default PostListPage;
