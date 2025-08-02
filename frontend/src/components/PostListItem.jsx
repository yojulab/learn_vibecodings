import React from 'react';
import { Link } from 'react-router-dom';

const PostListItem = ({ post }) => {
  return (
    <div className="bg-white border border-gray-200 p-6 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-200 flex flex-col gap-2">
      <h2 className="text-2xl font-bold mb-1 text-gray-900 hover:text-blue-600 transition-colors duration-150">
        <Link to={`/posts/${post.id}`}>{post.title}</Link>
      </h2>
      <p className="text-sm text-gray-500 mb-1">Category: <span className="font-medium text-blue-500">{post.category}</span></p>
      <p className="text-gray-700 line-clamp-3 prose prose-sm">{post.content.substring(0, 100)}...</p>
    </div>
  );
};

export default PostListItem;
